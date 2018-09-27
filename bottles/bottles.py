class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verse(self, count):
        if count == 1:
            return self._one_verse()
        elif count == 0:
            return self._zero_verse()
        return self._common_verse(count)

    def verses(self, start, end):
        return '\n\n'.join(self.verse(count) for count in range(start, end - 1, -1))

    def _common_verse(self, count):
        remaining = count - 1
        pluralized_bottles = self._pluralize_bottle(count)
        pluralized_remaining = self._pluralize_bottle(remaining)
        return ('{0} {1} of beer on the wall, {0} {1} of beer.\n'
                'Take one down and pass it around, {2} {3} of beer on the wall.').format(count, pluralized_bottles,
                                                                                         remaining,
                                                                                         pluralized_remaining)

    def _one_verse(self):
        return ('1 bottle of beer on the wall, 1 bottle of beer.\n'
                'Take it down and pass it around, no more bottles of beer on the wall.')


    def _zero_verse(self):
        return ('No more bottles of beer on the wall, no more bottles of beer.\n'
                'Go to the store and buy some more, 99 bottles of beer on the wall.')


    def _pluralize_bottle(self, count):
        return 'bottle' if count == 1 else 'bottles'
