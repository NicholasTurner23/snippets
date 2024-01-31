def reverse_letters(s):
    s_list = list(s)
    start, end = 0, len(s_list) - 1

    while start < end:
        while start < end and not s_list[start].isalpha():
            start += 1
        while start < end and not s_list[end].isalpha():
            end -= 1

        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1

    return ''.join(s_list)

# Example usage:
input_str = "a-bC-dEf=ghlj!!"
output_str = reverse_letters(input_str)
print(output_str)