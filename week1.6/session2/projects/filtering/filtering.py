def blur(img): 
    result = Image.create(img.width, img.height)

    for row in range(1, img.height-1):
        for col in range(1, img.width-1):
            
            total = 0 
            for x in range(row-1, row+2):
                for y in range(col-1, col+2):
                    total = img.get_pixel(x,y)

            average = total // 9 

            result.set_pixel(row, col, average)

    return result

    
