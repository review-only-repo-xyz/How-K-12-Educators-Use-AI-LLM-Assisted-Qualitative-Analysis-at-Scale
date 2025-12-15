# NOTE: i'm sure this function already exists, but i was in a hurry and it was easy to generate with AI
# TODO: rip this out and replace it with something pre-existing

import pandas as pd 

def normalize_nested_json_with_prefix(df):
    """
    Automatically detect and normalize all DataFrame columns containing nested dictionaries.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: New DataFrame with all nested columns normalized
    """
    result_df = df.copy()
    
    # Find columns containing dictionaries/nested structures
    nested_columns = []
    for column in result_df.columns:
        # Check first non-null value in the column
        first_valid = result_df[column].dropna().iloc[0] if not result_df[column].isna().all() else None
        if isinstance(first_valid, (dict, list)):
            nested_columns.append(column)
    
    if not nested_columns:
        print("No nested columns found in DataFrame")
        return result_df
    
    print(f"Found {len(nested_columns)} nested columns to normalize: {', '.join(nested_columns)}")
    
    for column in nested_columns:
        try:
            print(f"Normalizing column: '{column}'")
            
            # Handle potential empty dictionaries or null values
            valid_rows = result_df[column].dropna()
            if len(valid_rows) == 0:
                print(f"Skipping '{column}' - no valid data found")
                continue
                
            # Normalize the current column
            normalized = pd.json_normalize(result_df[column])
            
            # Add prefix to all columns from the normalized data
            normalized.columns = [f'{column}.{col}' for col in normalized.columns]
            
            # Update the result DataFrame
            result_df = pd.concat([
                result_df.drop([column], axis=1),
                normalized
            ], axis=1)
            
            print(f"Successfully normalized '{column}' into {len(normalized.columns)} columns")
            
        except Exception as e:
            print(f"Error normalizing '{column}': {str(e)}")
            continue
    
    return result_df

# Usage example:
# df = normalize_nested_columns(df)