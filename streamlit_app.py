import streamlit
import snowflake.connector
import pandas

streamlit.title("'Zena\'s Amazing Athleisure Catalog'")

#making sure requirements, secrets, and connections are all working together 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#FINAL Code we used for Zena’s Web Catalog Prototype

#put the dafta into a dataframe
df=pandas.dataframe(my_catalog)

# temp write the dataframe to the page so I Can see what I am working with
#streamlit.write(df)

# put the first column into a list
color_list = df[0].values.tolist()

# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website wherecolor_or_style = '" + option + "';")
df2 = my_cur.fetchone()

#image
streamlit.image(df2[0],
width=400,
caption= product_caption)

streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])

