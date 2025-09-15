import streamlit as st

# ---- Calibration chart ----
calibration = {
    "front": {
        164: 500, 285: 1000, 397: 1500, 504: 2000,
        611: 2500, 716: 3000, 820: 3500, 922: 4000,
        1026: 4500, 1129: 5000, 1234: 5500, 1339: 6000,
        1447: 6500, 1556: 7000, 1671: 7500, 1799: 8000
    },
    "middle": {
        160: 500, 280: 1000, 388: 1500, 493: 2000,
        597: 2500, 698: 3000, 800: 3500, 900: 4000,
        1000: 4500, 1100: 5000, 1200: 5500, 1302: 6000,
        1405: 6500, 1510: 7000, 1620: 7500, 1735: 8000
    },
    "rear": {
        173: 500, 292: 1000, 404: 1500, 511: 2000,
        618: 2500, 722: 3000, 825: 3500, 928: 4000,
        1031: 4500, 1134: 5000, 1237: 5500, 1342: 6000,
        1451: 6500, 1560: 7000, 1675: 7500, 1802: 8000
    }
}

def get_volume(chamber, dip):
    chamber = chamber.strip().lower()
    data = calibration[chamber]
    dips = sorted(data.keys())

    if dip in data:
        return data[dip]

    if dip < dips[0] or dip > dips[-1]:
        return None

    for i in range(len(dips) - 1):
        low_dip, high_dip = dips[i], dips[i+1]
        if low_dip <= dip <= high_dip:
            low_vol, high_vol = data[low_dip], data[high_dip]
            return round(low_vol + (dip - low_dip) * (high_vol - low_vol) / (high_dip - low_dip), 2)

    return None


st.title("HFO Measuring Server")
st.markdown("###### Powered by Sifat") 
st.markdown("### Lorry Number: Dhaka Metro Dha-11-02-74") 

chamber = st.selectbox("Select Chamber", ["Front", "Middle", "Rear"])
dip = st.number_input("Enter Dip (mm)", min_value=100, max_value=2000, step=1)

if st.button("Calculate Volume"):
    vol = get_volume(chamber, int(dip))
    if vol:
        st.success(f"{chamber} chamber at {int(dip)} mm = {vol} Liters")
    else:
        st.error("Dip out of range!")