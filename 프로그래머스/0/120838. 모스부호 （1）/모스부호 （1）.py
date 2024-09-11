def solution(letter):
    morse = { 
        '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f',
        '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
        '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
        '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
        '-.--':'y', '--..':'z'
    }
    
    decoded_message = ''.join(morse[code] for code in letter.split())
    return decoded_message
