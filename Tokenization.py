import nltk

from nltk.tokenize import word_tokenize



def split_tokens(message):

  message=message.lower()

  message = unicode(message, 'utf8') #convert bytes into proper unicode

  word_tokens =word_tokenize(message)

  return word_tokens





messages['tokenized_message'] = messages.apply(lambda row: split_tokens(row['message']),axis=1)
