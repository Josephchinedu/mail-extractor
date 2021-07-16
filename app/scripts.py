import re
from io import StringIO


class PastingIO(StringIO):
    def write_items_to_string(self, items, items_name: str):

        if items:
            for item in items:
                self.write(f"\t{item}\n")
        else:
            self.write(f"\n\tSorry, there are no {items_name}")

        self.write("\n")  # padding newline


def main(mailed):
    email_regex = re.compile(
        r"""(
            [a-zA-Z0-9._%+-]+           
            @                           
            [a-zA-Z0-9.-]+              
            (\.[a-zA-Z]{2,4})           
        )""",
        re.VERBOSE,
    )
    text = mailed
    

    output = PastingIO()


    matching_targets = {
        "emails": {"regex": email_regex,}
    }

    for target_name, target_dict in matching_targets.items():
        regex = target_dict["regex"]
        target_dict["results"] = [match[0] for match in regex.finditer(text)]
        output.write_items_to_string(target_dict["results"], target_name)

    match_summary = output.getvalue()

    return match_summary


if __name__ == "__main__":
    main()

    