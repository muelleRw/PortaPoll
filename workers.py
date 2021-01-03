from PySide2.QtCore import QObject, Signal, QRunnable, Slot

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        #self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            self.fn(*self.args, **self.kwargs)
        except Exception as error:
            print(error)
            #traceback.print_exc()
            #exctype, value = sys.exc_info()[:2]
            #self.signals.error.emit((exctype, value, traceback.format_exc()))
        #else:
        #    self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done