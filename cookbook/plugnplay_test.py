import plugnplai as pl

allurls = pl.get_plugins()

urls = [url for url in allurls if ("weather" in url)]
print("URLs: ",urls)

plugins = pl.Plugins.install_and_activate(urls[3])
print("Function: ",plugins.functions)
