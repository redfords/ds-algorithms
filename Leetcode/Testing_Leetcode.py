import a_Strings_Leetcode as a
import sys
import traceback

def a_strings():
    str = "255.100.50.0"
    a.defang_ip_addr(str)

    operations = ["X++","++X","--X","X--"]
    a.final_value_after_operations(operations)

    jewels = "aA"
    stones = "aAAbbbb"
    a.num_jewels_in_stones(jewels, stones)

    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    a.most_words_found(sentences)

    command = "G()(al)"
    a.interpret(command)

    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    a.restore_string(s, indices)

    s = "K1:L2"
    a.cells_in_range(s)

    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    a.decode_message(key, message)

    s = "Myself2 Me1 I4 and3"
    a.sort_sentence(s)

    sentence = "thequickbrownfoxjumpsoverthelazydog"
    a.check_if_pangram(sentence)

    word1  = ["a", "cb"]
    word2 = ["ab", "c"]
    a.array_strings_are_equal(word1, word2)

    words = ["gin","zen","gig","msg"]
    a.unique_morse_representations(words)

    s = "(1+(2*3)+((8)/4))+1"
    a.max_depth(s)

    s = "Hello how are you Contestant"
    k = 4
    a.truncate_sentence(s, k)

    s = "l|*e*et|c**o|*de|"
    a.count_asterisks(s)

    s = "Hello"
    a.to_lower_case(s)

    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    a.count_consistent_strings(allowed, words)

    s = "Let's take LeetCode contest"
    print(a.reverse_words(s))

if __name__=="__main__":
    try:
        a_strings()

    except Exception as e:
        print(traceback.format_exc())
        sys.exit()