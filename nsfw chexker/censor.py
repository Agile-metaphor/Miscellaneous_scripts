from nsfw_detector import predict
import os
import json




def iterate_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpeg', '.jpg')):
                image_path = os.path.join(root, file)
                print(predict.classify(model, image_path))
                with open("./fulldata.json", "w+", encoding="utf8") as filr:
                    filr.write(json.dumps(predict.classify(model, image_path)))
                    filr.close()
                with open("./fulldata.json", "r", encoding="utf8") as filt:
                    data = json.load(filt)


                # Iterate over the data
                for file_location, values in data.items():
                    if values['hentai'] > 0.5 or values['porn'] > 0.5:
                        # Delete the image file
                        os.remove(file_location)
                        print("Deleted:", file_location)


    # Iterate over the data
    for file_location, values in data.items():
        if values['hentai'] > 0.5 or values['porn'] > 0.5:
            # Delete the image file
            os.remove(file_location)
            print("Deleted:", file_location)

model = predict.load_model('./nsfw_mobilenet2.224x224.h5')
directory = 'C:\\Users\\dades\\Documents\\Projects\\Python\\ML\\stable-diffusion-webui\\models'
iterate_images(directory)