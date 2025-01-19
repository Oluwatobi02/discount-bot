import { useEffect, useState, useRef, useCallback } from 'react'
import { productFetcher } from '@/lib/utils'
import PriceCard, { ItemCardProp } from '@/components/card/PriceCard'

function Home() {
  const [items, setItems] = useState<ItemCardProp[]>([])
  let user_id = sessionStorage.getItem('user')
  const [pageState, setPageState] = useState({
    error: false,
    message: '',
    page: 1,
    hasMore: true,
    loading: false
  })

  const isFetching = useRef(false); 

  async function loadMoreProducts() {
    if (pageState.hasMore && !isFetching.current) {
      isFetching.current = true; 
      setPageState((prevPageState) => ({
        ...prevPageState,
        loading: true
      }))
      const products = await productFetcher(pageState.page, user_id= user_id || '')
      console.log(products)
      setItems((prevItems) => [...prevItems, ...products.data])
      setPageState((prevPageState) => ({
        ...prevPageState,
        hasMore: products.meta.hasMore,
        loading: false
      }))
      isFetching.current = false;
    }
  }

  useEffect(() => {
    loadMoreProducts()
  }, [pageState.page])

  const observer = useRef<IntersectionObserver | null>(null)

  const lastPostElementRef = useCallback(
    (node: Element | null) => {
      if (pageState.loading || !pageState.hasMore) return
      if (observer.current) observer.current.disconnect()

      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          setPageState((prevPageState) => ({
            ...prevPageState,
            page: prevPageState.page + 1
          }))
        }
      })

      if (node) observer.current.observe(node)
    },
    [pageState.loading, pageState.hasMore]
  )

  return (
    <div id="parent-scroll-container" className="h-screen overflow-y-auto overflow-x-hidden relative">
      <div className="p-6 bg-gray-50">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {items.map((item, index) => (
            <PriceCard
              key={index}
              _id={item._id}
              name={item.name}
              image={item.image}
              price={item.price}
              original_price={item.original_price}
              link={item.link}
              is_watching={item.is_watching}
              ref={items.length === index + 1 ? lastPostElementRef : null}
              
            />
          ))}
        </div>
        <div className="flex justify-center mt-8">
          {pageState.loading && (
            <div className="animate-spin rounded-full h-8 w-8 border-t-4 border-teal-600 border-solid"></div>
          )}
        </div>
      </div>
    </div>
  )
}

export default Home
