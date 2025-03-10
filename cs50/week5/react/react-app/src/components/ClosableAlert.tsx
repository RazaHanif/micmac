import { ReactNode } from "react"

interface Props {
    children: ReactNode;
    onClose: () => void;
}


const ClosableAlert = ({children, onClose}: Props) => {
  return (
    <div
      className="alert alert-primary alert-dismissible"
    >
      {children}
      <button
        type="button"
        onClick={onClose}
        className="btn-close"
      ></button>
    </div>
  )
}

export default ClosableAlert