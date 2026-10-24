import { useState } from "react";

import axios from "axios";


const UploadPDF = ()=>{

    const [file,setFile] = useState(null)

    const [loading,setLoading] = useState(false)

    const handleUpload = async ()=>{
        const formData = new FormData()

        formData.append(

            "file",

            file

        )

        try{
            setLoading(true)
            const response = await axios.post(

                "http://127.0.0.1:8000/upload",

                formData

            )
            alert(
                response.data.message
            )
        }
        catch(error){
            console.log(error)
        }
        finally{

            setLoading(false)

        }

    }

    return(

        <div className="bg-white p-6 rounded-xl shadow mb-6">
            <h2 className="text-xl font-semibold mb-4">

                Upload PDF

            </h2>
            <input

            type="file"

            accept=".pdf"

            onChange={(e)=>

                setFile(

                    e.target.files[0]

                )

            }

            />


            <button

            className="bg-blue-500 text-white px-4 py-2 rounded ml-4"

            onClick={handleUpload}
            >
                {

                    loading

                    ?

                    "Uploading..."

                    :

                    "Upload"

                }


            </button>


        </div>

    )


}


export default UploadPDF