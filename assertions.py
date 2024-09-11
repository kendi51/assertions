def assert_df_not_empty(df):
    assert not df.empty, "The DataFrame should not be empty."


def assert_df_dimensions_equal(df, height, width):
    assert_df_not_empty(df)
    assert df.shape == (
        height,
        width,
    ), f"The DataFrame dimensions: {df.shape} do not match provided dimensions: ({height}, {width})."


def assert_df_columns_equal(df, column_names):
    assert_df_not_empty(df)
    assert set(df.columns) == set(
        column_names
    ), f"The DataFrame columns do not match the columns provided."


def assert_no_duplicate_rows(df):
    assert_df_not_empty(df)
    assert (
        not df.duplicated().any()
    ), f"The Dataframe should not contain any duplicates."


def assert_no_null_values(df):
    assert_df_not_empty(df)
    assert not df.isna().any().any(), f"The DataFrame should not contain null values."


def assert_all_values_positive(df):
    assert_df_not_empty(df)
    assert (df >= 0).all().all(), f"The DataFrame should not have any negative values."
