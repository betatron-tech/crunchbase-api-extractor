from api_caller.api_queries import CrunchbaseExtractor









def main():
    cb_extractor = CrunchbaseExtractor()

    cb_extractor.get_organization_data('8villages')




if __name__ == "__main__":
    main()