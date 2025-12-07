import re

# Add new thing in file
def add_new_movie(movie_name, trailer_URL):
    file_name1="Movies.md"
    file_name2="Movie_Counter.Log.txt"
    # Read counter file for count number
    with open(file_name2, "r+") as counter_file:
        count=int(counter_file.read())

    # Add movie in file
    with open(file_name1, "r+") as movie_file:
        movie_file.write(f"{count+1}. {[movie_name]}{(trailer_URL)}\n")
        # counter_file.close()
        with open(file_name2, "w") as temp:
            temp.write(str(count+1))
            temp.close()
            counter_file.close()


# Remove symbols, spaces
def filter_name(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())

# Read files
def read_file(file_name):
    with open(file_name, "r+") as file:
        return file.read()

# Find pattern
def find_pattern(pattern, content):
    return re.findall(pattern, content)

# List matching letters in list and return it
def list_matching_letters(movie_name, dictionary_data):
    result=[value for key,value in dictionary_data.items() if movie_name in key]
    return result

##################################################
# Entry point
##################################################
if __name__=="__main__":
    while(True):
        print("1. Search Movies")
        print("2. Add Movies")
        print("3. Search TV SHow")
        print("4. Add TV Show")
        print("5. Search Book")
        print("6. Add Book")
        print("7. Exit")
        user_choice=int(input("Enter your choice: "))
        if user_choice==1:
            raw_movie_name=input("Enter Movie Name: ").lower().strip()
            print("-"*50)
            filtered_movie_name=filter_name(raw_movie_name)
            file_name="Movies.md"
            pattern=r"\[(.*?)\]"
            file_content=read_file(file_name)
            filtered_file_content=find_pattern(pattern, file_content)
            key_value_pair={filter_name(movie): movie for movie in filtered_file_content}
            matching_data=list_matching_letters(filtered_movie_name, key_value_pair)
            if matching_data:
                for i in matching_data:
                    print(i)
                print("-"*50)
            else:
                print("Not found anything!")
                print("-"*50)
        elif user_choice==2:
            add_new_movie("Sing is Bling!", "https://www.google.com")