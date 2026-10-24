import { useState } from "react"

import axios from "axios"


const ChatBox = ()=>{


    const [question,setQuestion]

    = useState("")


    const [answer,setAnswer]

    = useState("")


    const [loading,setLoading]

    = useState(false)




    const askQuestion = async ()=>{
        try{
            setLoading(true)
            const response = await axios.post(

                "http://127.0.0.1:8000/chat",

                {
                    question:question
                }
            )
            setAnswer(
                response.data.answer
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

        <div className="bg-white p-6 rounded-xl shadow">


            <h2 className="text-xl font-semibold mb-4">

                Ask Question

            </h2>
            <input

            className="border w-full p-3 rounded"

            type="text"

            value={question}

            placeholder="Ask something from PDF"

            onChange={(e)=>

                setQuestion(

                    e.target.value

                )

            }

            />
            <button

            className="bg-green-500 text-white px-5 py-2 rounded mt-4"

            onClick={askQuestion}

            >
                {

                    loading

                    ?

                    "Thinking..."

                    :

                    "Send"

                }


            </button>

            {

                answer &&

                <div className="mt-6">

                    <h3 className="font-semibold">

                        Answer

                    </h3>


                    <p className="mt-2">

                        {answer}

                    </p>

                </div>

            }

        </div>

    )
}
export default ChatBox