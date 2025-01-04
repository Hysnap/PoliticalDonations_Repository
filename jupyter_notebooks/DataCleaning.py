def DataCleaningEffect(df_original,df_cleaned,variables_applied_with_method):
  """
  This function compares the distribution of variables before and after data cleaning.

  Parameters:
  df_original (DataFrame): The original DataFrame before cleaning.
  df_cleaned (DataFrame): The DataFrame after cleaning.
  variables_applied_with_method (list): The list of variables that the cleaning method was applied to.
  """

  flag_count=1 # Counter to keep track of the plot number
  
  # Identify categorical variables in the original DataFrame
  categorical_variables = df_original.select_dtypes(exclude=['number']).columns 

  # Loop over the variables that the cleaning method was applied to
  for set_of_variables in [variables_applied_with_method]:
    print("\n=====================================================================================")
    print(f"* Distribution Effect Analysis After Data Cleaning Method in the following variables:")
    print(f"{set_of_variables} \n\n")
  
    # For each variable, plot its distribution before and after cleaning
    for var in set_of_variables:
      if var in categorical_variables:  # If the variable is categorical, use a barplot
        # Create DataFrames for the original and cleaned data
        df1 = pd.DataFrame({"Type":"Original","Value":df_original[var]})
        df2 = pd.DataFrame({"Type":"Cleaned","Value":df_cleaned[var]})
        # Concatenate the two DataFrames
        dfAux = pd.concat([df1, df2], axis=0)
        # Create the plot
        fig , axes = plt.subplots(figsize=(15, 5))
        sns.countplot(hue='Type', data=dfAux, x="Value",palette=['#432371',"#FAAE7B"])
        axes.set(title=f"Distribution Plot {flag_count}: {var}")
        plt.xticks(rotation=90)
        plt.legend() 

      else: # If the variable is numerical, use a histogram
        # Create the plot
        fig , axes = plt.subplots(figsize=(10, 5))
        sns.histplot(data=df_original, x=var, color="#432371", label='Original', kde=True,element="step", ax=axes)
        sns.histplot(data=df_cleaned, x=var, color="#FAAE7B", label='Cleaned', kde=True,element="step", ax=axes)
        axes.set(title=f"Distribution Plot {flag_count}: {var}")
        plt.legend()