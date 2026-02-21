class HistoryStore:
    _instance = None
    _history = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryStore, cls).__new__(cls)
        return cls._instance

    def save(self, question, answer):
        self._history.insert(0, {"question": question, "answer": answer})
        self._history = self._history[:10]

    def get(self):
        return self._history

    def clear(self):
        self._history = []
