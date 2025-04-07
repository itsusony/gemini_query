from google import genai
import argparse, os, re

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"
if not GEMINI_API_KEY: raise ValueError("GEMINI_API_KEY not set")

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folders", type=str, default="")
parser.add_argument("-q", "--query", type=str, default="")
parser.add_argument("-d", "--dry_run", action="store_true")
parser.add_argument("-w", "--white_lists", type=str, default=".py,.html")
args = parser.parse_args()

folder_list = [f.strip() for f in args.folders.split(',') if f.strip()]
if not args.query or not folder_list: raise ValueError("query or folders not set")

white_lists = args.white_lists.split(',')
for folder in folder_list:
    if not os.path.exists(folder): raise ValueError(f"Folder not found: {folder}")

def get_files_in_folder(folders, white_lists):
    ret = []
    for folder in folders:
        for root, _, files in os.walk(folder):
            if ".git" in root: continue
            for f in files:
                if f.startswith("../"): continue
                path = os.path.join(root, f)
                if os.path.splitext(path)[-1].lower() in white_lists:
                    try:
                        ret.append({"path": path, "content": open(path).read()})
                    except: pass
    return ret

file_content = "\n".join([f"path: {f['path']}\ncontent: {f['content']}\n"
                         for f in get_files_in_folder(folder_list, white_lists)])

if args.dry_run: exit(0)

print(genai.Client(api_key=GEMINI_API_KEY).models.generate_content(
    model=MODEL_NAME,
    contents=[args.query, file_content]).text)
