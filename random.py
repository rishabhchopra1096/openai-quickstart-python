listing_images = {}

for listingId in range(1, 45):
    listing_images[listingId] = [
       "require('../../assets/images/listings/"+str(listingId)+"/"+str(listingId)+"-main.png')",
       "require('../../assets/images/listings/"+str(listingId)+"/"+str(listingId)+"-Exteriors.png')",
       "require('../../assets/images/listings/"+str(listingId)+"/"+str(listingId)+"-Livingroom.png')",
       "require('../../assets/images/listings/"+str(listingId)+"/"+str(listingId)+"-Bedroom.png')",
       "require('../../assets/images/listings/"+str(listingId)+"/"+str(listingId)+"-Bathroom.png')",
    ]
    

for i in range(1,45):
    print(r"images: [")
    for image in listing_images[i]:
        print(rf"{image},")
    print("],")
    print("\n\n")