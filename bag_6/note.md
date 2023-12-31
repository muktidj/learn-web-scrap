## Note 1: 
In this first project, we're going to scrape the website Audible. Recently the website slightly changed its HTML.

**In minute 4:57 of the next video instead of writing the XPath shown in the video, we'll use the following XPath: .//li[contains(@class, "productListItem")]**

**This means that the "products" variable will be:**

**products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')**

That's it! The rest of the code remains the same. Remember that this change should be also considered for the rest of the videos in this section.

## Note 2: 
In the videos, we scrape Audible US. In case your browser redirects you to your local version of Audible, please use a VPN to get Audible US. There are many free VPNs out there. TunnelBear work fine for me