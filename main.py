from image_scraper import search_and_download


if __name__ == '__main__':
    print("****** Process Started ******")
    search_and_download(search_term='graffiti', driver_path='webdriver/chromedriver', target_path='./images',
                        number_images=50, headless=True)
