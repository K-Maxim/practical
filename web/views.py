from django.shortcuts import render, HttpResponse

# Create your views here.

alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}


# test
def all_letters(request):
    return HttpResponse(f'{alphabet}', content_type="text/plain", charset="utf-8")


# low task 1
def letter(request, letter):
    if letter in alphabet:
        one_letter = alphabet[letter]
        return render(request, '../templates/letter.html', {'letter': one_letter})
    return render(request, '../templates/letter.html', {'letter': 'Такой буквы нет'})


# low task 2
def find_letter(request):
    letter = request.GET.get('letter')
    return HttpResponse(f'{alphabet[letter]}', content_type="text/plain", charset="utf-8")
    # return render(request, '../templates/find_letter.html', {'letter': alphabet[letter]})


# low task 3
def check_letter(request, letter, word):
    cher_word = alphabet[letter]
    if cher_word == word:
        return HttpResponse(f'{"True"}', content_type="text/plain", charset="utf-8")
    return HttpResponse(f'{"False"}', content_type="text/plain", charset="utf-8")


# low task 4
def between_letters(request):
    from_letter = request.GET.get('from')
    to_letter = request.GET.get('to')
    first_index_letter = ''.join(alphabet.keys()).find(from_letter)
    second_index_letter = ''.join(alphabet.keys()).find(to_letter)
    if first_index_letter < second_index_letter:
        return HttpResponse(f'{"".join(alphabet.keys())[first_index_letter + 1:second_index_letter]}',
                            content_type="text/plain", charset="utf-8")
    elif first_index_letter > second_index_letter:
        return HttpResponse(f'{"".join(alphabet.keys())[second_index_letter + 1:first_index_letter]}',
                            content_type="text/plain", charset="utf-8")
    return HttpResponse('-', content_type="text/plain", charset="utf-8")


# low task 5
def get_some(request, number):
    if number > 0:
        return HttpResponse(f'{"".join(alphabet.keys())[:number]}',
                            content_type="text/plain", charset="utf-8")
    elif number > len(''.join(alphabet.keys())):
        return HttpResponse(f'{"".join(alphabet.keys())}',
                            content_type="text/plain", charset="utf-8")
    return HttpResponse('-', content_type="text/plain", charset="utf-8")


# low task 6
def limit_letters(request):
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    all_keys = ''.join(alphabet.keys())
    if limit > len(all_keys) or offset > len(all_keys):
        return HttpResponse('-', content_type="text/plain", charset="utf-8")
    range_letters = all_keys[offset:limit + offset].lower()
    return HttpResponse(f"{''.join(range_letters)}", content_type="text/plain", charset="utf-8")