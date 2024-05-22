import datasets


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        out_doc = {'labels': [chr(ord('A') + idx) for idx in range(len(doc['choices']))],
                   'label': chr(ord('A') + doc['choices'].index(doc['answer']))}
        return out_doc

    return dataset.map(_process_doc)
