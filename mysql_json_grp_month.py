import mysql.connector
import json
from datetime import datetime
from collections import defaultdict

def get_mysql_data():
    # Establish MySQL connection
    mydb = mysql.connector.connect(
        host="192.168.0.38",        # Replace with your MySQL server address
        user="hakim",     # Replace with your MySQL username
        password="sap123ok", # Replace with your MySQL password
        database="trs"  # R
    )

    #if mydb.is_connected():
        #print("message: mysql connected")
        # logger.info(f"mysql mydb connected")
    cursor = mydb.cursor()
    # sql = """SELECT * FROM note1"""
    sql = """SELECT COUNT(trs.trs.PosInID) as Count_vehicle,trs.trs.ClassID,trs.trs.PosOutID,trs.trs.IsCust,trs.trs.TimeIn as TimeIn,trs.trs.TimeOut,SUM(trs.trs.RateOut) as Rate,mst.class.Vehicle FROM trs.trs JOIN mst.class ON trs.trs.ClassID = mst.class.ID WHERE trs.trs.TimeIn >= '2024-01-01 00:00:00' AND trs.trs.TimeIn <= '2024-02-01 00:00:00' AND trs.trs.Status = 1 AND trs.trs.IsCust = 0 GROUP BY YEAR(trs.trs.TimeIn),MONTH(trs.trs.TimeIn),trs.trs.ClassID,trs.trs.IsCust"""
    
    cursor.execute(sql)
    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    json_str = json.dumps(data, default=str)
    data_from_json = json.loads(json_str)
    #return data_from_json
    #print(json_str)    
    #return json_str 
    #data2 = json_str[0]
    #print(data_from_json[0]['TimeIn'])
    #datetime_obj = datetime.strptime(data_from_json[0]['TimeIn'], "%Y-%m-%d %H:%M:%S")

    # Output the datetime object
    #print(datetime_obj)

    #data = get_mysql_data()
    #print(data)

    # Group data by Year and Month
    grouped_data = defaultdict(list)

    for record in data_from_json:
        # Parse TimeIn to extract Year and Month
        time_in = datetime.strptime(record['TimeIn'], "%Y-%m-%d %H:%M:%S")
        year_month = (time_in.year, time_in.month)
        
        # Append the record to the corresponding group
        grouped_data[year_month].append(record)

    # Convert grouped data to JSON format
    json_data = [
        {
            "Year": year,
            "Month": month,
            "data": records
        }
        for (year, month), records in grouped_data.items()
    ]

    # Convert to JSON string
    # output_json = json.dumps(json_data, indent=4)
    output_json = json.dumps(json_data, indent=4)
    return output_json
    # Print JSON
    #print(output_json)

#get_mysql_data()