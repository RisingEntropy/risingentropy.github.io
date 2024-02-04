import os
import sys

escape_list = list("\\`*_")
def create_index(current_dir, father_dir=""):
    html_code = """
    <head>
    <title>File lists</title>
    </head>
    <body>
    """
    if father_dir != "":
        html_code += f"<a href=\"../\">Father Directory</a><br>"
    file_lists = []
    for file in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, file)):
            create_index(os.path.join(current_dir, file), current_dir)
            file_lists.append(f"<a href=\"./{file}/\">{file}</a><br>")
        else:
            file_lists.append(f"<a href=\"./{file}\">{file}</a><br>")
    html_code+="\n".join(file_lists)
    html_code+="\n</body>"
    with open(os.path.join(current_dir,"index.html"), "w") as f:
        f.write(html_code)

def escape(text, file_name):
    cnt = 0
    state = "NORMAL"
    result = ""
    grave_accent_count = 0  # ` is called grave_accent_count, used to clearify code block
    is_last_dollar = False
    is_last_disp_block = False
    for char in text:
        if char == "$":
            cnt+=1
        char_escaped = char
        if state=="NORMAL":
            if char=="$":
                state = "IN_MATHJAX"  # No matter $ or $$, a $ means going into a mathjax block
                char_escaped = char
            elif char=="`":
                grave_accent_count+=1
                if grave_accent_count==3:
                    state="IN_CODE_BLOCK"
                    grave_accent_count = 0
                char_escaped = char
            else:
                state = "NORMAL"
                grave_accent_count = 0
                char_escaped = char
        elif state=="IN_MATHJAX":
            if char=="$":
                if is_last_dollar and not is_last_disp_block:
                    state = "IN_DISPLAYMATH"  # go out of inline mathjax block
                else:
                    is_last_disp_block = False
                    state = "NORMAL"
                char_escaped = char
            elif char in escape_list:
                char_escaped = "\\"+char
            else:
                state = "IN_MATHJAX"
                char_escaped = char
        elif state=="IN_DISPLAYMATH":
            if char=="$":
                is_last_disp_block = True
                state = "IN_MATHJAX" # when processing the third $ in $$ $$ pair, just directly go into $ $ state, the reuse is ok since it will go to noraml
                # state in the next character.
            char_escaped = char # do no modification
        elif state=="IN_CODE_BLOCK":
            if char=="`":
                grave_accent_count+=1
                if grave_accent_count==3:
                    state="NORMAL"  # go out of code block
                    grave_accent_count = 0
                char_escaped = char
            else:
                char_escaped = char
        result+=char_escaped
        is_last_dollar = char=="$"
    if cnt%2!=0:
        print(f"Waring:$ mismatch in file:{file_name}")
    if state!="NORMAL":
        print(f"Waring:state machine does not reset to NORMAL, current state:{state}, file:{file_name}")
    return result.replace("{{","{% raw %} {{ {% endraw %}").replace("}}","{% raw %} }} {% endraw %}")

def main():
    print(os.getcwd())
    dirs_to_escape = sys.argv[1:]
    for path in dirs_to_escape:
        try:
            for file in os.listdir(path):
                print(f"processing: {os.path.join(path, file)}")
                content = ""
                with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                    content = f.read()
                content = escape(content, os.path.join(path, file))
                with open(os.path.join(path, file), "w", encoding="utf-8") as f:
                    f.write(content)
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
    print("done!")

if __name__=="__main__":
    main()
    create_index("site/single_pages")

