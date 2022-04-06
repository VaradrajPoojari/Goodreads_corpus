import pandas as pd

GOODREADS_PATH = './data/data.csv'


class GoodReadsDataManager:
    def __init__(self, data):
        self._raw_data = data

        self._raw_data['rating'] = self._raw_data['rating']
        self._raw_data['rating'] = self._raw_data['rating'].fillna(2.5)

        self._unique_fields = {
            'genres': list(self._raw_data['genre'].unique()),
            'annotations': list(self._raw_data['Final Annotation'].unique()),
            'titles': list(self._raw_data['title'].unique()),
            'authors': list(self._raw_data['author'].unique()),
            'ratings': list(self._raw_data['rating'].unique()),
        }

        self._reviews = self._raw_data[['author', 'genre', 'Final Annotation', 'title', 'review', 'rating']]
        self._reviews = self._reviews.rename(columns={'Final Annotation': 'emotion'})

    def get_field_values(self, field, filter_key: str = None):
        """

        :param field:
        :param filter_key:
        :return:
        """
        if not filter_key or not len(filter_key):
            # Rating rating
            return sorted(self._unique_fields[field.lower()])

        return sorted([entry for entry in self._unique_fields[field.lower()] if filter_key.strip() in entry])

    def get_reviews(self, filters, strict=True):
        """
        :type filters_dict: object

        """
        
        filters_dict = dict([filter for filter in filters if filter[1] and len(filter[1])])
        # TODO: if strict is false, get filters to lowercase
        

        temp_df = self._reviews
        for field, values in filters_dict.items():
            if field == 'rating':
                values = [int(value) for value in values]
            if strict:
                # Filter based on "hard" filters - needs a full match
                print(temp_df[field].isin(values))
                temp_df = temp_df.loc[temp_df[field].isin(values)]
            else:
                # Filter as a search, returns when the row contains the filter as a substring
                print(field)
                print(values)
                # print(temp_df[field])
                print()
                if field == 'rating':
                    temp_df = temp_df.loc[temp_df[field].isin(values)]
                else:
                    temp_df = temp_df.loc[temp_df[field].apply(str.lower).str.contains('|'.join(values).lower()), :]
        temp_df = temp_df.sort_values(by=['title'], ascending=True)
        return temp_df.to_dict(orient='records')
