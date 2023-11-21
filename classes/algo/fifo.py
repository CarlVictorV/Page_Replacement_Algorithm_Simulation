from classes import page as p


class FIFO(p.Page):
    def __init__(self, page_sequence, frame_count, page_count):
        super().__init__(page_sequence, frame_count, page_count)
        self.fifo()

    def fifo(self):
        """
        Simulates the FIFO algorithm.
        """
        index = 0
        for page in self.page_sequence:
            # Check if page is in a frame
            if self.check_for_page(page):
                self.page_hit_events(index)
            # Check if there is an empty frame
            elif self.check_for_empty_frame():
                self.page_fault_events(index)
                self.add_page_to_empty_frame(page, index)
            # If there is no empty frame and page is not in a frame
            # Find the oldest page and replace it
            else:
                self.page_fault_events(index)
                self.page_replacement_event(
                    index, page, self.find_oldest_page())

            index += 1

        self.calculate_rates()

    def print_fifo_table(self):
        """
        Prints the FIFO table.
        """
        print("FIFO Table")
        self.print_sequence()
        self.print_frames()
        self.print_rates()
