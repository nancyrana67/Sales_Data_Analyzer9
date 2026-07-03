import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.current_plot = None
        print("\nSales Data Analyzer Initialized Successfully!")

    def __del__(self):
        print("\nProgram Closed Successfully!")

    # ----------------------------
    # LOAD DATA
    # ----------------------------
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("\nDataset Loaded Successfully!")
        except FileNotFoundError:
            print("\nFile Not Found!")
        except Exception as e:
            print(e)

    # ----------------------------
    # EXPLORE DATA
    # ----------------------------
    def explore_data(self):

        if self.data is None:
            print("Load dataset first!")
            return

        while True:

            print("\n========== Explore Data ==========")
            print("1. Display First 5 Rows")
            print("2. Display Last 5 Rows")
            print("3. Display Column Names")
            print("4. Display Data Types")
            print("5. Display Basic Information")
            print("6. Back")

            ch = input("Enter Choice : ")

            if ch == "1":
                print(self.data.head())

            elif ch == "2":
                print(self.data.tail())

            elif ch == "3":
                print(self.data.columns)

            elif ch == "4":
                print(self.data.dtypes)

            elif ch == "5":
                print(self.data.info())

            elif ch == "6":
                break

            else:
                print("Invalid Choice!")

    # ----------------------------
    # CLEAN DATA
    # ----------------------------
    def clean_data(self):

        if self.data is None:
            print("Load dataset first!")
            return

        while True:

            print("\n========== Handle Missing Data ==========")
            print("1. Show Missing Values")
            print("2. Fill Missing Values with Mean")
            print("3. Drop Missing Rows")
            print("4. Replace Missing with Specific Value")
            print("5. Back")

            choice = input("Enter Choice : ")

            if choice == "1":

                missing = self.data.isnull().sum()

                if missing.sum() == 0:
                    print("No Missing Values Found!")

                else:
                    print(missing)

            elif choice == "2":

                numeric = self.data.select_dtypes(include=np.number).columns

                for col in numeric:
                    self.data[col].fillna(
                        self.data[col].mean(),
                        inplace=True
                    )

                print("Missing Values Filled!")

            elif choice == "3":

                self.data.dropna(inplace=True)
                print("Rows Deleted Successfully!")

            elif choice == "4":

                value = input("Enter Value : ")
                self.data.fillna(value, inplace=True)
                print("Missing Values Replaced!")

            elif choice == "5":
                break

            else:
                print("Invalid Choice!")

    # ----------------------------
    # NUMPY ARRAY
    # ----------------------------
    def numpy_operations(self):

        if self.data is None:
            print("Load dataset first!")
            return

        print("\n========== NumPy Operations ==========")

        numeric = self.data.select_dtypes(include=np.number)

        arr = numeric.to_numpy()

        print("\nNumPy Array\n")
        print(arr)

        print("\nShape :", arr.shape)

        print("\nFirst Row")
        print(arr[0])

        print("\nFirst Two Rows")
        print(arr[:2])

        print("\nFirst Column")
        print(arr[:, 0])

        print("\nLast Row")
        print(arr[-1])

    # ----------------------------
    # MATHEMATICAL OPERATIONS
    # ----------------------------
    def mathematical_operations(self):

        if self.data is None:
            print("Load dataset first!")
            return

        numeric = self.data.select_dtypes(include=np.number)

        print("\nAddition")
        print(numeric + 10)

        print("\nSubtraction")
        print(numeric - 10)

        print("\nMultiplication")
        print(numeric * 2)

        print("\nDivision")
        print(numeric / 2)

    # ----------------------------
    # COMBINE DATA
    # ----------------------------
    def combine_data(self, other_file):

        if self.data is None:
            print("Load Dataset First!")
            return

        try:

            other = pd.read_csv(other_file)

            print("\n1. Concat")
            print("2. Merge")
            print("3. Join")

            ch = input("Choice : ")

            if ch == "1":
                result = pd.concat([self.data, other])

            elif ch == "2":

                key = input("Common Column : ")
                result = pd.merge(self.data, other, on=key)

            elif ch == "3":
                result = self.data.join(other)

            else:
                print("Invalid Choice!")
                return

            print(result.head())

        except Exception as e:
            print(e)

    # ----------------------------
    # SPLIT DATA
    # ----------------------------
    def split_data(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        column = input("Column Name : ")

        if column not in self.data.columns:
            print("Invalid Column!")
            return

        groups = dict(tuple(self.data.groupby(column)))

        for key, value in groups.items():
            print(f"\n------ {key} ------")
            print(value.head())

        # ----------------------------
    # SEARCH, SORT & FILTER
    # ----------------------------
    def search_sort_filter(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        while True:

            print("\n========== Search / Sort / Filter ==========")
            print("1. Search")
            print("2. Sort")
            print("3. Filter")
            print("4. Back")

            ch = input("Enter Choice : ")

            if ch == "1":

                col = input("Column Name : ")

                if col not in self.data.columns:
                    print("Invalid Column!")
                    continue

                value = input("Search Value : ")

                result = self.data[
                    self.data[col].astype(str).str.contains(value, case=False)
                ]

                print(result)

            elif ch == "2":

                col = input("Sort By : ")

                if col not in self.data.columns:
                    print("Invalid Column!")
                    continue

                order = input("Ascending (y/n): ")

                asc = True if order.lower() == "y" else False

                print(self.data.sort_values(by=col, ascending=asc))

            elif ch == "3":

                col = input("Filter Column : ")

                if col not in self.data.columns:
                    print("Invalid Column!")
                    continue

                value = input("Value : ")

                print(self.data[self.data[col].astype(str) == value])

            elif ch == "4":
                break

            else:
                print("Invalid Choice!")

    # ----------------------------
    # AGGREGATE FUNCTIONS
    # ----------------------------
    def aggregate_functions(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        numeric = self.data.select_dtypes(include=np.number)

        print("\n========== Aggregate Functions ==========")

        print("\nSum")
        print(numeric.sum())

        print("\nMean")
        print(numeric.mean())

        print("\nMaximum")
        print(numeric.max())

        print("\nMinimum")
        print(numeric.min())

        print("\nCount")
        print(numeric.count())

    # ----------------------------
    # STATISTICAL ANALYSIS
    # ----------------------------
    def statistical_analysis(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        numeric = self.data.select_dtypes(include=np.number)

        print("\n========== Statistical Analysis ==========")

        print("\nDescribe")
        print(numeric.describe())

        print("\nStandard Deviation")
        print(numeric.std())

        print("\nVariance")
        print(numeric.var())

        print("\nMedian")
        print(numeric.median())

        print("\n25%,50%,75% Quantiles")
        print(numeric.quantile([0.25,0.50,0.75]))

    # ----------------------------
    # PIVOT TABLE
    # ----------------------------
    def create_pivot_table(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        index = input("Index Column : ")
        values = input("Values Column : ")

        if index not in self.data.columns:
            print("Invalid Index!")
            return

        if values not in self.data.columns:
            print("Invalid Value!")
            return

        pivot = pd.pivot_table(
            self.data,
            index=index,
            values=values,
            aggfunc=np.sum
        )

        print("\nPivot Table\n")
        print(pivot)

        # ----------------------------
    # VISUALIZATION
    # ----------------------------
    def visualize_data(self):

        if self.data is None:
            print("Load Dataset First!")
            return

        numeric = self.data.select_dtypes(include=np.number)

        if numeric.empty:
            print("No Numeric Data Found!")
            return

        columns = numeric.columns.tolist()

        while True:

            print("\n========== Visualization ==========")
            print("1. Bar Chart")
            print("2. Line Chart")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Subplots")
            print("8. Heatmap")
            print("9. Box Plot")
            print("10. Save Current Figure")
            print("11. Back")

            choice = input("Enter Choice : ")

            # ---------------- BAR ----------------
            if choice == "1":

                plt.figure(figsize=(8,5))
                plt.bar(self.data.index, numeric[columns[0]])
                plt.title("Bar Chart")
                plt.xlabel("Index")
                plt.ylabel(columns[0])
                plt.grid(True)
                self.current_plot = plt
                plt.show()

            # ---------------- LINE ----------------
            elif choice == "2":

                plt.figure(figsize=(8,5))
                plt.plot(numeric[columns[0]], marker="o")
                plt.title("Line Chart")
                plt.xlabel("Index")
                plt.ylabel(columns[0])
                plt.grid(True)
                self.current_plot = plt
                plt.show()

            # ---------------- SCATTER ----------------
            elif choice == "3":

                if len(columns) < 2:
                    print("Need at least 2 numeric columns.")
                    continue

                plt.figure(figsize=(8,5))
                plt.scatter(
                    numeric[columns[0]],
                    numeric[columns[1]]
                )
                plt.title("Scatter Plot")
                plt.xlabel(columns[0])
                plt.ylabel(columns[1])
                plt.grid(True)
                self.current_plot = plt
                plt.show()

            # ---------------- PIE ----------------
            elif choice == "4":

                numeric[columns[0]].head(5).plot(
                    kind="pie",
                    autopct="%1.1f%%"
                )

                plt.ylabel("")
                plt.title("Pie Chart")
                self.current_plot = plt
                plt.show()

            # ---------------- HISTOGRAM ----------------
            elif choice == "5":

                plt.figure(figsize=(8,5))
                plt.hist(numeric[columns[0]], bins=10)
                plt.title("Histogram")
                plt.xlabel(columns[0])
                plt.ylabel("Frequency")
                self.current_plot = plt
                plt.show()

            # ---------------- STACK PLOT ----------------
            elif choice == "6":

                if len(columns) < 2:
                    print("Need at least 2 numeric columns.")
                    continue

                x = np.arange(len(numeric))

                plt.figure(figsize=(8,5))
                plt.stackplot(
                    x,
                    numeric[columns[0]],
                    numeric[columns[1]]
                )

                plt.title("Stack Plot")
                plt.xlabel("Index")
                plt.legend(columns[:2])
                self.current_plot = plt
                plt.show()

            # ---------------- SUBPLOTS ----------------
            elif choice == "7":

                fig, ax = plt.subplots(2,1,figsize=(8,8))

                ax[0].plot(numeric[columns[0]])
                ax[0].set_title("Line Plot")

                ax[1].hist(numeric[columns[0]])
                ax[1].set_title("Histogram")

                plt.tight_layout()
                self.current_plot = plt
                plt.show()

            # ---------------- HEATMAP ----------------
            elif choice == "8":

                plt.figure(figsize=(8,5))
                sns.heatmap(numeric.corr(), annot=True)
                plt.title("Heatmap")
                self.current_plot = plt
                plt.show()

            # ---------------- BOXPLOT ----------------
            elif choice == "9":

                plt.figure(figsize=(8,5))
                sns.boxplot(data=numeric)
                plt.title("Box Plot")
                self.current_plot = plt
                plt.show()

            # ---------------- SAVE ----------------
            elif choice == "10":

                if self.current_plot is None:
                    print("No Plot Available!")
                else:
                    filename = input("Enter File Name : ")
                    self.current_plot.savefig(filename + ".png")
                    print("Plot Saved Successfully!")

            elif choice == "11":
                break

            else:
                print("Invalid Choice!")

                