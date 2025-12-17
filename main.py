import re
import sys

# Add new tv show
def add_new_tv_show(tv_show_name, trailer_URL):
    file_name="TV_Shows.md"
    patt=r"(\d+\.)"
    with open(file_name, 'r') as f1:
        text=f1.read()
        raw_sr_number=re.findall(patt, text)
        temp=re.sub(r"[^0-9]", '', raw_sr_number[len(raw_sr_number)-1])
        temp=int(temp)+1
        temp=str(temp)

    with open(file_name, 'a') as f2:
        f2.write(f"{temp}. [{tv_show_name}]({trailer_URL})\n")
    f1.close()
    f2.close()
    return 1


# Add new thing in file
def add_new_movie(movie_name, trailer_URL):
    file_name="Movies.md"
    patt=r"(\d+\.)"
    with open(file_name, 'r') as f1:
        text=f1.read()
        raw_sr_number=re.findall(patt, text)
        temp=re.sub(r"[^0-9]", '', raw_sr_number[len(raw_sr_number)-1])
        temp=int(temp)+1
        temp=str(temp)

    with open(file_name, 'a') as f2:
        f2.write(f"{temp}. [{movie_name}]({trailer_URL})\n")
    f1.close()
    f2.close()
    return 1


# Remove symbols, spaces
def filter_name(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())

# Read files
def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
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
        print("3. Search TV Show")
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
            movie_name=input("Enter Movie Name: ").strip().capitalize()
            trailer_url=input("Enter Trailer URL: ").strip()
            if add_new_movie(movie_name, trailer_url):
                print(f"Successfull added: {movie_name}")
            else:
                print(f"Oops! Something went wrong!")
        elif user_choice==3:
            raw_movie_name=input("Enter Show Name: ").lower().strip()
            print("-"*50)
            filtered_show_name=filter_name(raw_movie_name)
            file_name="TV_Shows.md"
            pattern=r"\[(.*?)\]"
            file_content=read_file(file_name)
            filtered_file_content=find_pattern(pattern, file_content)
            key_value_pair={filter_name(movie): movie for movie in filtered_file_content}
            matching_data=list_matching_letters(filtered_show_name, key_value_pair)
            if matching_data:
                for i in matching_data:
                    print(i)
                print("-"*50)
            else:
                print("Not found anything!")
                print("-"*50)


        elif user_choice==4:
            tv_show_name=input("Enter TV Show Name: ").strip().capitalize()
            trailer_url=input("Enter Trailer URL: ").strip()
            if add_new_tv_show(tv_show_name, trailer_url):
                print(f"Successfully added: {tv_show_name}")
            else:
                print(f"Oops! Something went wrong!")
        elif user_choice==5:
            raw_book_name=input("Enter Book Name: ").lower().strip()
            print("-"*50)
            filtered_book_name=filter_name(raw_book_name)
            file_name="Books.md"
            pattern=r"\[(.*?)\]"
            file_content=read_file(file_name)
            filtered_file_content=find_pattern(pattern, file_content)
            key_value_pair={filter_name(movie): movie for movie in filtered_file_content}
            matching_data=list_matching_letters(filtered_book_name, key_value_pair)
            if matching_data:
                for i in matching_data:
                    print(i)
                print("-"*50)
            else:
                print("Not found anything!")
                print("-"*50)
        elif user_choice==7:
            sys.exit()