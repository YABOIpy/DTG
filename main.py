from source.utils import thread, util

if __name__ == '__main__':
    thread.create_threads(
        cfg=util.Utilities.config("config.json"),
        proxies=util.Utilities.readfile(
            direct="proxies.txt",
            level=0
        )
    )
