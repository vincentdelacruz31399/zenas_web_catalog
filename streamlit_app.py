import streamlit
import snowflake.connector
import pandas

streamlit.title("'Zena\'s Amazing Athleisure Catalog'")

#making sure requirements, secrets, and connections are all working together 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#FINAL Code we used for Zena’s Web Catalog Prototype

#put the dafta into a dataframe
df=pandas.dataframe(my_catalog)

# temp write the dataframe to the page so I Can see what I am working with
streamlit.write(df)
