import webview

def open_preview(url):
    webview.create_window("Preview", url)
    webview.start()
