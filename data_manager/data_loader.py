import pandas as pd


class DataLoader:
    @classmethod
    def load(cls, file_location: str):
        """
        Loads a CSV file as Panda DF
        :param file_location:
        :return:
        """
        try:
            return pd.read_csv(file_location)
        except Exception as e:
            raise Exception(f'Unable to load file {file_location}: {e}')