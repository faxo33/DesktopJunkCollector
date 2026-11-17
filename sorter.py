import os
import shutil


desktop = os.path.join(os.path.expanduser("~"), "Desktop")
destination = os.path.join(desktop, "PDFs")


os.makedirs(destination, exist_ok=True)
count = 0


for item in os.listdir(desktop):

    full_path = os.path.join(desktop, item)

    if os.path.isfile(full_path) and item.lower().endswith(".pdf"):

        new_path = os.path.join(destination, item)

       
        if not os.path.exists(new_path):
            shutil.move(full_path, new_path)
            count += 1
            print("Moved:", item)
        else:
            print("Skipped (already exists):", item)


print("PDFs moved:", count)
print("Finished!")
