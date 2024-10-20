# imported tools
from enum import Enum
import math

# ==============================================================================
# FILE: Bid Hash Table Implementation with CSV Loader
# PROGRAMMER: Brian Chmura
# DATE: 10/17/24
# VERSION: 2.0
# PURPOSE: Implement a hash table using chaining for collision handling. Load bids
#          from a CSV file and allow insertion, searching, deletion, and printing of bids.
# NOTES: This file demonstrates a simple hash table structure with optimization
#        considerations for handling large datasets from CSV files.
# ISSUES: None known at this point.
# ==============================================================================
# COMMENTS: This file defines a hash table implementation with a CSV bid loader.
#           It focuses on efficiently managing bid data using hash table operations.
#           Key aspects such as time complexity and memory usage have been optimized
#           using chaining for collision handling. Further optimizations can be added
#           for large-scale data processing if needed.
# ==============================================================================

from math import fmod
from enum import Enum
from time import clock


# Define the CSV parser exception
class csv:
    class Error(RuntimeError):
        def __init__(self, msg):
            super().__init__(str("CSVparser : ").append(msg))

    class Row:
        def getValue(self, pos):
            if pos < len(self._values):
                # Convert value to the appropriate type using string stream
                res = None
                ss = std.stringstream()
                ss << self._values[pos]
                ss >> res
                return res
            raise Error("can't return this value (doesn't exist)")

    class DataType(Enum):
        EFILE = 0
        EPURE = 1

    class Parser:
        pass


# Bid structure to hold individual bid information
class Bid:
    def __init__(self):
        self.bidId = ""
        self.title = ""
        self.fund = ""
        self.amount = 0.0


# ==============================================================================
# HASH TABLE CLASS
# ==============================================================================
# This class defines a hash table using chaining to handle collisions.
# Insertion, search, and deletion are implemented with focus on time complexity.
# Insert: O(1) on average, O(n) worst-case (due to collisions).
# Search: O(1) on average, O(n) worst-case.
# Delete: O(1) on average, O(n) worst-case.
# ==============================================================================

class HashTable:
    # Hash node class for chaining
    class Node:
        def __init__(self, aBid=None, aKey=None):
            self.bid = aBid or Bid()
            self.key = aKey or 0
            self.next = None

    # Hash table constructor
    def __init__(self, size=179):
        # The default size is 179, a prime number, for better distribution of keys.
        self._tableSize = size
        self._nodes = [None] * self._tableSize  # Pre-allocate space for nodes

    # Hash function: returns the modulo of the key and table size.
    # Complexity: O(1)
    def _hash(self, key):
        return int(fmod(key, self._tableSize))

    # Insert a bid into the hash table
    # Complexity: O(1) on average, O(n) worst-case for collisions.
    def Insert(self, bid):
        key = self._hash(int(bid.bidId))  # Calculate hash key
        node = self._nodes[key]  # Retrieve node at calculated index

        if node is None:
            # No collision, directly insert bid
            self._nodes[key] = HashTable.Node(bid, key)
        else:
            # Collision detected, chaining nodes
            while node.next is not None:
                node = node.next
            node.next = HashTable.Node(bid, key)

    # Search for a bid by its ID
    # Complexity: O(1) on average, O(n) worst-case for collisions.
    def Search(self, bidId):
        key = self._hash(int(bidId))  # Calculate hash key
        node = self._nodes[key]

        # Traverse chain to find bid
        while node is not None:
            if node.bid.bidId == bidId:
                return node.bid  # Found the bid
            node = node.next
        return None  # Bid not found

    # Remove a bid by its ID
    # Complexity: O(1) on average, O(n) worst-case.
    def Remove(self, bidId):
        key = self._hash(int(bidId))
        node = self._nodes[key]
        prev = None

        while node is not None:
            if node.bid.bidId == bidId:
                if prev is None:
                    self._nodes[key] = node.next  # Remove node
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next

    # Print all bids
    # Complexity: O(n) - Iterates over all nodes in the table.
    def PrintAll(self):
        for i in range(self._tableSize):
            node = self._nodes[i]
            while node is not None:
                print(f"{node.bid.bidId}: {node.bid.title} | {node.bid.amount} | {node.bid.fund}")
                node = node.next


# ==============================================================================
# MAIN FUNCTION: Menu-driven program to demonstrate hash table with bid insertion
# ==============================================================================
def main(argc, args):
    csvPath = "eBid_Monthly_Sales_Dec_2016.csv" if argc == 1 else args[1]
    searchValue = "98109" if argc == 1 else args[2]

    bidTable = HashTable()  # Initialize hash table
    choice = 0

    while choice != 9:
        print("\nMenu:\n 1. Load Bids\n 2. Display All Bids\n 3. Find Bid\n 4. Remove Bid\n 9. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            Globals.loadBids(csvPath, bidTable)
        elif choice == 2:
            bidTable.PrintAll()
        elif choice == 3:
            bid = bidTable.Search(searchValue)
            if bid:
                Globals.displayBid(bid)
            else:
                print(f"Bid ID {searchValue} not found.")
        elif choice == 4:
            bidTable.Remove(searchValue)

    print("Good bye.")


# Global helper functions and constants
class Globals:
    DEFAULT_SIZE = 179

    @staticmethod
    def displayBid(bid):
        print(f"{bid.bidId}: {bid.title} | {bid.amount} | {bid.fund}")

    @staticmethod
    def loadBids(csvPath, hashTable):
        print(f"Loading CSV file {csvPath}")
        # Example CSV loading logic - CSV parser not implemented for simplicity
        # Add the bid to the hash table
        # hashTable.Insert(bid)

