# DataHandleWithPandas

A comprehensive Python project demonstrating advanced data handling and analysis operations using pandas, numpy, and data visualization libraries.

## Overview

This project showcases advanced pandas operations and data analysis techniques including:
- Complex DataFrame creation with realistic employee data
- Statistical analysis and correlation studies
- Advanced grouping and aggregation operations
- Data cleaning and missing value handling
- Multi-level data filtering and querying
- Custom metrics and binning operations
- Data export and summary generation

## Features

### Data Generation
- **Synthetic Dataset**: 100 employee records with realistic distributions
- **Multiple Data Types**: Numeric, categorical, boolean, and datetime columns
- **Missing Values**: Intentionally introduced for realistic data cleaning scenarios

### Analysis Capabilities
- **Comprehensive Statistics**: Descriptive statistics across all numeric columns
- **Department Analysis**: Salary and performance breakdowns by department
- **Correlation Analysis**: Relationship studies between numeric variables
- **Performance Metrics**: High performer identification and analysis
- **Remote Work Analysis**: Comparative statistics for remote vs in-office employees
- **Salary Banding**: Custom categorization of salary ranges
- **Tenure Calculations**: Employee tenure analysis from hire dates

### Data Processing
- **Missing Value Imputation**: Smart filling using department-based medians
- **Data Validation**: Realistic bounds enforcement for age and other metrics
- **Advanced Filtering**: Complex multi-condition data queries
- **Export Functionality**: CSV export of processed data and summaries

## Files

- `data.py` - Main script containing comprehensive data analysis pipeline
- `employee_data_processed.csv` - Generated output file with processed employee data
- `department_summary.csv` - Generated summary statistics by department

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib (for future visualization enhancements)

## Installation

```bash
pip install pandas numpy matplotlib
```

## Usage

Run the comprehensive analysis script:

```bash
python data.py
```

## Output

The script generates detailed analysis including:

1. **Basic Data Overview**: Dataset dimensions and data types
2. **Statistical Summary**: Comprehensive descriptive statistics
3. **Missing Values Analysis**: Identification and quantification of missing data
4. **Department Analysis**: Performance and salary metrics by department
5. **Correlation Matrix**: Relationships between numeric variables
6. **High Performer Analysis**: Identification of top performers (score > 4.0)
7. **Remote Work Statistics**: Comparative analysis of remote vs in-office employees
8. **Advanced Filtering Examples**: Complex query demonstrations
9. **Custom Metrics**: Salary banding and tenure calculations
10. **Data Cleaning Results**: Before/after missing value treatment
11. **Export Confirmation**: File generation notifications

## Sample Dataset

The generated dataset includes:
- **Employee ID**: Unique identifier (1-100)
- **Name**: Employee names (Employee_1, Employee_2, etc.)
- **Age**: Normally distributed ages (22-65 years)
- **Salary**: Realistic salary distribution ($35K-$110K range)
- **Department**: IT, HR, Finance, Marketing, Operations
- **Years Experience**: Exponentially distributed experience levels
- **Performance Score**: Rating scale 1.0-5.0 (with some missing values)
- **Hire Date**: Random dates over 4-year period
- **Remote Status**: Boolean flag for remote work arrangement

## Advanced Features

- **Reproducible Results**: Uses numpy seed for consistent output
- **Realistic Distributions**: Employs statistical distributions for data generation
- **Data Quality**: Includes missing values and outliers for real-world scenarios
- **Multiple Analysis Layers**: From basic statistics to advanced multi-dimensional analysis
- **Export Ready**: Generates clean datasets for further analysis or reporting