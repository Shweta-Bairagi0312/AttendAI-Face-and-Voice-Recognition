# import streamlit as st

# from supabase import create_client, Client

# supabase:Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]
# )

# import streamlit as st


# from supabase import create_client, Client

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]
# )

# import streamlit as st
# from supabase import create_client, Client

# print(st.secrets["SUPABASE_URL"])

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]
# )

# import streamlit as st
# from supabase import create_client, Client

# print(st.secrets["SUPABASE_URL"])

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]
# )

# response = supabase.table("teachers").select("*").execute()

# print(response)


import streamlit as st
from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)