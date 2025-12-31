
class MycustomException(Exception):
    def __init__(self,error:Exception):
        self.error = error

        if isinstance(error,str):
            super().__init__(error)
            return
        tb = error.__traceback__

        while tb.tb_next is not None:
            tb = tb.tb_next

        filename = tb.tb_frame.f_code.co_filename
        lineno = tb.tb_lineno

        message = f"🚫🚫🚫🚫🚫🚫🚫🚫 Error occured at {filename}-{lineno}; with message {error} "

        super().__init__(message)

if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        raise(MycustomException(e))



