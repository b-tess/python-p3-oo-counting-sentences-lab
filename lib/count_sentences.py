#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    if type(value) == str:
      self.value = value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    interim_value = self.value.replace('!', '.').replace('?', '.').split('.')
    new_value = [item for item in interim_value if item != '']

    return len(new_value)
