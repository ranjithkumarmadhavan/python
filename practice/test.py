text = 'Theres a voice that keeps on calling me. Down the road, thats where Ill always be. Every stop I make, I make a new friend. Cant stay for long, just turn around and Im gone again. Maybe tomorrow, Ill want to settle down, Until tomorrow, I’ll just keep moving on.'

search_list = ['voice', 'Until', 'gone']

def compare(text,search_list):
    result = {}
    for item in search_list:
        result[item] = text.count(item)
    return result

print(compare(text, search_list))