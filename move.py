import os
k=1
for filename in os.listdir("C:\\Users\\Admin\\Documents\\Resize\\Extracted2"):
    f = os.path.join("C:\\Users\\Admin\\Documents\\Resize\\Extracted2", filename)
    l = os.path.join("C:\\Users\\Admin\\Documents\\Resize\\Extracted", filename)
    print('Processing image ', k, ' of ', len(os.listdir("C:\\Users\\Admin\\Documents\\Resize\\Extracted2")))
    if os.path.isfile(f):
        os.rename(f,l)
        k+=1