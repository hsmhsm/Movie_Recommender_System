#------------------------------------------------------------------------------#
# import required python modules here                                          #
#------------------------------------------------------------------------------#
import csv
import sys


#------------------------------------------------------------------------------#
# open data base files                                                         #
#------------------------------------------------------------------------------#
def open_data_base_files():

  # open user data base file
  try:
    user_file = open("./movie_data_set/ml-100k/u.user", 'r', \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The user data base file 'u.user' does not exist, exiting " +
          "gracefully.\n")
    sys.exit()

  # open movie data base file
  try:
    movie_file = open("./movie_data_set/ml-100k/u.item", 'r',  \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The movie data base file 'u.item' does not exist, exiting "
          + "gracefully.\n")
    sys.exit()

  # open rating data base file
  try:
    rating_file = open("./movie_data_set/ml-100k/u.data", 'r', \
                                                          encoding="ISO-8859-1")
  except IOError:
    print("\nError: The rating data base file 'u.data' does not exist, exiting "
           + "gracefully.\n")
    sys.exit()

  return user_file, movie_file, rating_file
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# close data base files                                                        #
#------------------------------------------------------------------------------#
def close_data_base_files(user_file, movie_file, rating_file):

  user_file.close()
  movie_file.close()
  rating_file.close()
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# read data base files                                                         #
#------------------------------------------------------------------------------#
def read_data_base_files(user_file, movie_file, rating_file):

  # read user data base file
  try:
    user_data_base = list(csv.reader(user_file, delimiter='|'))
  except csv.Error:
    print("\nError: in reading user data base file, exiting gracefully.\n")
    sys.exit()

  # read movie data base file
  try:
    movie_data_base = list(csv.reader(movie_file, delimiter='|'))
  except csv.Error:
    print("\nError: in reading movie data base file, exiting gracefully.\n")
    sys.exit()

  # read rating data base file
  try:
    rating_data_base = list(csv.reader(rating_file, delimiter='\t'))
  except csv.Error:
    print("\nError: in reading rating data base file, exiting gracefully.\n")
    sys.exit()

  return user_data_base, movie_data_base, rating_data_base
#------------------------------------------------------------------------------#