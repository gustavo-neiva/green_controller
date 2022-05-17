from .app import run
   
if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(e)