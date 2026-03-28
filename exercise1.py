def add_element(input_data):
    def find_max_depth(obj, current_depth):
        max_d = current_depth
        
        if isinstance(obj, (list, tuple)):
            for item in obj:
                max_d = max(max_d, find_max_depth(item, current_depth + 1))
        elif isinstance(obj, dict):
            for value in obj.values():
                max_d = max(max_d, find_max_depth(value, current_depth + 1))
        
        return max_d

    def modify(obj, current_depth, target_depth):
        if current_depth == target_depth:
            if isinstance(obj, list):
                next_value = 1
                if len(obj) > 0:
                    last_element = obj[-1]
                    if isinstance(last_element, (int, float)):
                        next_value = last_element + 1
                obj.append(next_value)
            return obj

        if isinstance(obj, list):
            for i in range(len(obj)):
                obj[i] = modify(obj[i], current_depth + 1, target_depth)
        elif isinstance(obj, tuple):
            temp_list = list(obj)
            for i in range(len(temp_list)):
                temp_list[i] = modify(temp_list[i], current_depth + 1, target_depth)
            return tuple(temp_list)
        elif isinstance(obj, dict):
            for key in obj:
                obj[key] = modify(obj[key], current_depth + 1, target_depth)
        
        return obj

    max_depth = find_max_depth(input_data, 0)
    
    return modify(input_data, 0, max_depth)

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"key": [5, 6], "text": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = add_element(input_list)
    print(output_list)
