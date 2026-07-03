from Sales_Data_Analyzer9 import sales_data_analyzer


def main():

    analyzer = sales_data_analyzer()

    while True:

        print("\n" + "=" * 55)
        print("        SALES DATA ANALYZER SYSTEM")
        print("=" * 55)
        print("1. Load CSV Dataset")
        print("2. Explore Dataset")
        print("3. Handle Missing Values")
        print("4. NumPy Operations")
        print("5. Mathematical Operations")
        print("6. Combine DataFrames")
        print("7. Split DataFrame")
        print("8. Search / Sort / Filter")
        print("9. Aggregate Functions")
        print("10. Statistical Analysis")
        print("11. Create Pivot Table")
        print("12. Data Visualization")
        print("13. Exit")
        print("=" * 55)

        choice = input("Enter Your Choice : ")

        # ------------------------------
        # LOAD DATASET
        # ------------------------------
        if choice == "1":

            file = input("Enter CSV File Name : ")

            try:
                analyzer.load_data(file)
            except Exception as e:
                print("Error :", e)

        # ------------------------------
        # EXPLORE
        # ------------------------------
        elif choice == "2":

            analyzer.explore_data()

        # ------------------------------
        # CLEAN DATA
        # ------------------------------
        elif choice == "3":

            analyzer.clean_data()

        # ------------------------------
        # NUMPY
        # ------------------------------
        elif choice == "4":

            analyzer.numpy_operations()

        # ------------------------------
        # MATHEMATICAL
        # ------------------------------
        elif choice == "5":

            analyzer.mathematical_operations()

        # ------------------------------
        # COMBINE
        # ------------------------------
        elif choice == "6":

            second = input("Enter Second CSV File : ")
            analyzer.combine_data(second)

        # ------------------------------
        # SPLIT
        # ------------------------------
        elif choice == "7":

            analyzer.split_data()

        # ------------------------------
        # SEARCH / SORT / FILTER
        # ------------------------------
        elif choice == "8":

            analyzer.search_sort_filter()

        # ------------------------------
        # AGGREGATE
        # ------------------------------
        elif choice == "9":

            analyzer.aggregate_functions()

        # ------------------------------
        # STATISTICS
        # ------------------------------
        elif choice == "10":

            analyzer.statistical_analysis()

        # ------------------------------
        # PIVOT TABLE
        # ------------------------------
        elif choice == "11":

            analyzer.create_pivot_table()

        # ------------------------------
        # VISUALIZATION
        # ------------------------------
        elif choice == "12":

            analyzer.visualize_data()

        # ------------------------------
        # EXIT
        # ------------------------------
        elif choice == "13":

            print("\nThank You For Using Sales Data Analyzer!")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()