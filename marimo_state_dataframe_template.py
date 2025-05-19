import marimo

__generated_with = "0.13.7-dev22"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pandas import DataFrame, concat
    return DataFrame, concat, mo


@app.cell
def _(DataFrame):
    df = DataFrame({'id': [1, 2, 3], 'name': ['a', 'b', 'c']})
    return (df,)


@app.cell
def _(df, mo):
    get_df, set_df = mo.state(df)
    return get_df, set_df


@app.cell
def _(mo):
    enter_data = mo.ui.dictionary(
        {
            'id': mo.ui.slider(start=4, stop=10, step=1, label='ID'),
            'name': mo.ui.text(value='something', label='NAME'),
        }
    ).form(submit_button_label='Add Row Data')
    enter_data
    return (enter_data,)


@app.cell
def _(DataFrame, concat, enter_data, get_df, set_df):
    def add_data(event):
        new_row = DataFrame([enter_data.value])
        return set_df(lambda df: concat([get_df(), new_row], ignore_index=True))
    return (add_data,)


@app.cell
def _(add_data, mo):
    mo.ui.button(label='press', on_click=add_data)
    return


@app.cell
def _(get_df):
    get_df()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
