def load_urls_from_file(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readline()
            return content
    except:
        print("the file " + file_path + " could not be found");
        exit(2)


def load_page(url: str):
    # TODO: add the code that reads the url
    pass


def scrape_page(page_contents: str):
    # TODO: analyze the text
    pass
