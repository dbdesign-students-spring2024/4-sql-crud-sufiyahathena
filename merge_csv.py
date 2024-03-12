import pandas as pd

messages_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/messages.csv'
stories_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/stories.csv'
merged_csv_path = '/Users/sufiyahathena/Desktop/4-sql-crud-sufiyahathena/4-sql-crud-sufiyahathena/posts.csv'

messages_df = pd.read_csv(messages_csv_path)
stories_df = pd.read_csv(stories_csv_path)

stories_df['RecipientID'] = None
messages_df['Visible'] = True
stories_df['Visible'] = True

posts_df = pd.concat([messages_df, stories_df], ignore_index=True)

posts_df.to_csv(merged_csv_path, index=False)

print(f'Merged posts saved to {merged_csv_path}')
